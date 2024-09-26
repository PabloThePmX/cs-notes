package GestaoBiblioteca;

import java.util.Comparator;
import java.util.Scanner;

//projeto finalizado em: https://github.com/Sckelic/gerenciaBiblioteca
//praticamente uma classe view, pois é usada apenas para interagir com o usuário.
public class Main {
    static public Biblioteca biblio = new Biblioteca();
    static public Scanner input = new Scanner(System.in);

    private static void adicionar(){
        Livro livro = new Livro();
        System.out.print("Informe o título do livro: ");
        livro.setTitulo(input.nextLine());
        System.out.print("Informe o nome do autor: ");
        livro.setAutor(input.nextLine());
        System.out.print("Informe o ano de publicação: ");
        livro.setAnoPublicacao(input.nextInt());
        input.nextLine();
        System.out.print("Informe o número de páginas: ");
        livro.setnPaginas(input.nextInt());
        input.nextLine();

        try{
            biblio.adicionar(livro);
            System.out.println("Livro adicionado com sucesso!");
        } catch(Exception e){
            System.out.println("ERRO " + e.getMessage());
        }

        input.nextLine();
    }

    private static void listar(){
        var livros = biblio.pesquisarTodos();
        //ordena de forma alfabetica
        livros.sort(Comparator.comparing(Livro::getTitulo));
        for (Livro livro : livros) {
            System.out.println("Titulo: " + livro.getTitulo());
            System.out.println("Autor: " + livro.getAutor());
            System.out.println("Ano: " + livro.getAnoPublicacao());
            System.out.println("N. Páginas: " + livro.getnPaginas());
        }
    }

    private static int inputNumerico(String mensagem){
        int valor = 0;
        boolean entradaValida = false;
        System.out.println(mensagem);

        do{    
            String valorStr = input.nextLine();
            try{
                valor = Integer.parseInt(valorStr);
                entradaValida = true;
            }catch(Exception e){
                System.out.println("Erro. Por favor um número inteiro.");
            }
        } while(!entradaValida);
        return valor;
    }

    public static void main(String[] args) {
        String menu = """
                SISTEMA DE GERENCIAMENTO DE BIBLIOTECA
                1 - Adicionar novo livro;
                2 - Listar todos os livros;
                3 - Pesquisar livro;
                4 - Remover livro;

                0 - Sair;
                """;
        int opcao;
        do{
            opcao = inputNumerico(menu);
            switch (opcao) {
                case 1:
                    adicionar();
                    break;
                
                case 2:
                    listar();
                    break;
                
                case 3:
                    break;

                case 4:
                    break;
                
                case 0:
                    break;
            
                default:
                    System.out.println("Opção Inválida!");
                    input.nextLine();
                    break;
            }
        } while(opcao != 0);
    }
}
