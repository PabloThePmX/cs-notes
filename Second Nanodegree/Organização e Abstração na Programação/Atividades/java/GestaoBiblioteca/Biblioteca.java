package GestaoBiblioteca;

import java.util.ArrayList;
import java.util.List;

//service (api)
public class Biblioteca {
    private List<Livro> acervo = new ArrayList<>();

    public void adicionar(Livro livro) throws Exception{
        if(livro.getTitulo() == null || livro.getTitulo().isEmpty())
            throw new Exception("Não é permitido cadastrar livro sem título.");
        for (Livro livroItem : acervo) {
            if (livroItem.getTitulo().equalsIgnoreCase(livro.getTitulo()))
                throw new Exception("Já existe livro cadastrado com este título.");
            else
                acervo.add(livro);
        }
    }

    public  List<Livro> pesquisarPorTitulo(String titulo){
        List<Livro> livrosEncontrados = new ArrayList<>();
        for(Livro livro : acervo){
            if(livro.getTitulo().toLowerCase().contains(titulo.toLowerCase()))
                livrosEncontrados.add(livro);
        }
        return livrosEncontrados;
    }

    public void removerPorTitulo(String titulo){
        for(Livro livro : acervo){
            if(livro.getTitulo().equalsIgnoreCase(titulo))
                acervo.remove(livro);
        }
    }

    public List<Livro> pesquisarTodos(){
        return acervo;
    }
}
