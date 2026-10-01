"""Gera o site de estudo (index.html) a partir dos 3 arquivos .md desta pasta.

Uso:  python build_site.py     (requer:  pip install markdown)
Edite os .md e rode de novo para atualizar o site.
"""
import json
import re
from pathlib import Path

import markdown

HERE = Path(__file__).parent


def md(text):
    return markdown.markdown(text.strip(), extensions=["tables", "fenced_code"])


def inline(text):
    html = md(text)
    return re.sub(r"^<p>(.*)</p>$", r"\1", html, flags=re.S)


def split_extra(q):
    """'➕ pergunta' -> (True, 'pergunta')"""
    q = q.strip()
    return (True, q[1:].strip()) if q.startswith("➕") else (False, q)


def read(name):
    return (HERE / name).read_text(encoding="utf-8")


# ---------- Resumo ----------
def parse_resumo():
    text = read("1 - Resumo.md")
    text = re.sub(r"^# Gestão de Projetos.*\n", "", text)
    parts = re.split(r"^# (Aula \d+): (.+)$", text, flags=re.M)
    sections = []
    intro = parts[0].replace("---", "").strip()
    sections.append({"id": 0, "title": "Mapa geral", "html": md(intro)})
    for i in range(1, len(parts), 3):
        n = int(parts[i].split()[1])
        body = parts[i + 2].strip()
        body = re.sub(r"\n---\s*$", "", body).strip()
        sections.append({"id": n, "title": parts[i + 1].strip(), "html": md(body)})
    return sections


# ---------- Flashcards ----------
def split_aulas(text):
    parts = re.split(r"^## Aula (\d+): (.+)$", text, flags=re.M)
    for i in range(1, len(parts), 3):
        yield int(parts[i]), parts[i + 1].strip(), parts[i + 2]


def parse_cards():
    cards = []
    pat = re.compile(
        r"\*\*(\d+)\. (.+?)\*\*\s*<details><summary>Resposta</summary>(.*?)</details>", re.S
    )
    for aula, _, body in split_aulas(read("2 - Flashcards.md")):
        for m in pat.finditer(body):
            extra, q = split_extra(m.group(2))
            cards.append(
                {"id": int(m.group(1)), "aula": aula, "q": inline(q), "a": md(m.group(3)), "extra": extra}
            )
    return cards


# ---------- Quiz ----------
def parse_quiz():
    qs = []
    pat = re.compile(
        r"\*\*(\d+)\. (.+?)\*\*\s*((?:- [A-D]\) [^\n]+\n?)+)\s*<details><summary>Gabarito</summary>\s*\*\*([A-D])\.\*\*\s*(.*?)</details>",
        re.S,
    )
    for aula, _, body in split_aulas(read("3 - Quiz.md")):
        for m in pat.finditer(body):
            opts = re.findall(r"- ([A-D])\) (.+)", m.group(3))
            extra, q = split_extra(m.group(2))
            qs.append(
                {
                    "id": int(m.group(1)),
                    "aula": aula,
                    "extra": extra,
                    "q": inline(q),
                    "opts": [{"k": k, "t": inline(t)} for k, t in opts],
                    "ans": m.group(4),
                    "exp": inline(m.group(5)),
                }
            )
    return qs


def aula_titles():
    titles = {}
    for aula, title, _ in split_aulas(read("2 - Flashcards.md")):
        titles[aula] = title
    return titles


def main():
    data = {
        "resumo": parse_resumo(),
        "cards": parse_cards(),
        "quiz": parse_quiz(),
        "aulas": aula_titles(),
    }
    print(f"{len(data['resumo'])} seções, {len(data['cards'])} flashcards, {len(data['quiz'])} questões")
    n_cards = len(re.findall(r"^\*\*\d+\. ", read("2 - Flashcards.md"), flags=re.M))
    n_quiz = len(re.findall(r"^\*\*\d+\. ", read("3 - Quiz.md"), flags=re.M))
    assert len(data["cards"]) == n_cards and len(data["quiz"]) == n_quiz, "algum cartão/questão não foi lido, confira o formato nos .md"
    print(f"extras: {sum(c['extra'] for c in data['cards'])} cartões, {sum(q['extra'] for q in data['quiz'])} questões")
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    html = (HERE / "template.html").read_text(encoding="utf-8").replace("/*__DATA__*/null", payload)
    (HERE / "index.html").write_text(html, encoding="utf-8")
    print("index.html gerado")


if __name__ == "__main__":
    main()
