package GestaoBibliotecaFinal;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

public class Biblioteca {
    //BD em memória
    private List<Livro> acervo = new ArrayList<>();

    public void adicionar(Livro livro) throws Exception{
        if (livro.getTitulo() == null || livro.getTitulo().isEmpty())
            throw new Exception("Não é permitido cadastrar livro sem titulo...");
        if (livro.getAutor() == null || livro.getAutor().isEmpty())
            throw new Exception("Não é possível cadastrar um livro sem autor...");
        if (livro.getAnoPublicacao() <= 1400 || livro.getAnoPublicacao() > LocalDate.now().getYear())
            throw new Exception("Não é um ano de publicacão válido...");
        if (livro.getnPaginas() <= 0)
            throw new Exception("Cadastre um livro com pelos menos uma página...");
        for (Livro livroAcervo : acervo) {
            if (livroAcervo.getTitulo().equalsIgnoreCase(livro.getTitulo()))
                throw new Exception("Já existe um livro cadastrado com este titulo...");
        }
        acervo.add(livro);
    }

    public List <Livro> pesquisar(String titulo) throws Exception{
        return pesquisar(titulo, null);
    }

    public List <Livro> pesquisar(String titulo, String autor) throws Exception{
        List<Livro> livrosEncontrados = new ArrayList<>();
        boolean livroExiste = false;
        for (Livro livro : acervo) {
            if (livro.getTitulo().toLowerCase().contains(titulo.toLowerCase())) {
                if(autor == null || livro.getAutor().toLowerCase().contains(autor.toLowerCase())){
                    livrosEncontrados.add(livro);
                    livroExiste = true;
                }
            }
        }

        if(!livroExiste)
            throw new Exception("O livro não existe.");

        return livrosEncontrados;
    }

    public void removerPorTitulo(String titulo) throws Exception{
        boolean livroRemovido = false;
        for (Livro livro : acervo) {
            if (livro.getTitulo().equalsIgnoreCase(titulo)){
                acervo.remove(livro);
                livroRemovido = true;
                break;
            }
        }

        if(!livroRemovido)
        throw new Exception("O livro não pertence ao acervo");
    }

    public List<Livro> pesquisarTodos(){
        return this.acervo;
    }
    
}