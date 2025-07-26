package GestaoBibliotecaFinal;

import java.util.Comparator;
import java.util.List;
import java.util.Scanner;

public class Main {
    static Biblioteca biblio = new Biblioteca();
    static Scanner input = new Scanner(System.in);

    public static void clear() {
        System.out.print("\033[H\033[2J");
        System.out.flush();
    }

    private static int inputNumerico(String mensagem) {
        int valor = 0;
        boolean entradaValida = false;
        System.out.print(mensagem);
        do {
            String valorStr = input.nextLine();
            try {
                valor = Integer.parseInt(valorStr);
                entradaValida = true;
            } catch (Exception e) {
                System.out.println("Erro! informe um numero inteiro!");
            }
        } while (!entradaValida);
        return valor;
    }

    private static void listarInformacoes(List<Livro> livros){
        clear();
        System.out.println("======== LISTA DE LIVROS =========");
        for (Livro livro : livros) {
            // System.out.println("Título: " + livro.getTitulo());
            // System.out.println("Autor: " + livro.getAutor());
            // System.out.println("Ano: " + livro.getAnoPublicacao());
            // System.out.println("N. Páginas: " + livro.getnPaginas());
            System.out.println(livro.toString());
            System.out.printf("\n");
        }
    }

    private static void pesquisarPorTitulo(){
        System.out.print("Informe o título do livro a ser buscado: ");
        String titulo = input.nextLine();
        try{
            var livros = biblio.pesquisar(titulo);
            listarInformacoes(livros);
        } catch(Exception e){
            System.out.println("Erro: " + e.getMessage());
        }
        input.nextLine();
    }

    private static void removerPorTitulo(){
        System.out.print("Informe o título do livro a ser removido: ");
        String tituloremove = input.nextLine();
        try{
            biblio.removerPorTitulo(tituloremove);
            System.out.println("Livro removido com sucesso!!");
        } catch(Exception e){
            System.out.println("Erro: " + e.getMessage());
        }
        input.nextLine();
    }

    private static void listar() {
        // List<Livro> livros = biblio.pesquisarTodos();
        var livros = biblio.pesquisarTodos();
        livros.sort(Comparator.comparing(Livro::getTitulo));
        listarInformacoes(livros);
        input.nextLine();
    }

    private static void adicionar() {
        Livro novoLivro;
        System.out.println("======== ADICIONANDO NOVO LIVRO ========");
        int tipoLivro = inputNumerico("Qual o tipo do livro: (1) Livro, (2) Digital");
        if(tipoLivro == 1){
            novoLivro = new LivroFisico();
        }
        else if (tipoLivro == 2){
            novoLivro = new LivroDigital();
        } else{
            //transformar essa classe em abstract
            novoLivro = new Livro();
        }

        System.out.print("Informe o título do livro: ");
        String titulo = input.nextLine();
        novoLivro.setTitulo(titulo);

        System.out.print("Informe o nome do autor: ");
        novoLivro.setAutor(input.nextLine());

        novoLivro.setAnoPublicacao(inputNumerico("Informe o ano de publicação: "));

        novoLivro.setnPaginas(inputNumerico("Informe o número de páginas: "));

        if (tipoLivro == 1){
            ((LivroFisico) novoLivro).setnExemplares(inputNumerico("Insira o número de exemplares: "));
            System.out.print("Digite as dimensões: ");
            ((LivroFisico) novoLivro).setDimensoes(input.nextLine());
        } else if(tipoLivro == 2){
            System.out.print("Digite o formato do arquivo");
            ((LivroDigital) novoLivro).setFormatoArquivo(input.nextLine());
            ((LivroDigital) novoLivro).setTamanhoArquivo(inputNumerico("Insira o tamanho do arquivo: "));
        }

        try {
            biblio.adicionar(novoLivro);
            System.out.println("Livro adicionado com Sucesso!");
        } catch (Exception e) {
            System.out.println("Erro: " + e.getMessage());
        }
        input.nextLine(); // espera o usuário dar um enter para continuar
        clear();
    }

    public static void main(String[] args) {
        clear();
        String menu = 
            """
        SISTEMA DE GERENCIAMENTO DE BIBLIOTECA

        Escolha uma das opções:
            1 - Adicionar novo livro;
            2 - Listar todos os livros;
            3 - Pesquisar livro;
            4 - Remover livro;
            0 - Sair;
            """;
        int opcao;
        do {
            // System.out.println(menu);
            // opcao = input.nextInt();
            // input.nextLine(); // limpar buffer
            opcao = inputNumerico(menu);
            switch (opcao) {
                case 0:
                    clear();
                    System.out.println("VOLTE SEMPRE!!!");
                    break;
                case 1:
                    clear();
                    adicionar();
                    clear();
                    break;
                case 2:
                    clear();
                    listar();
                    clear();
                    break;
                case 3:
                    clear();
                    pesquisarPorTitulo();
                    clear();
                    break;
                case 4:
                    clear();
                    removerPorTitulo();
                    clear();
                    break;
                default:
                    clear();
                    System.out.println("Opção Inválida!!!");
                    input.nextLine();
                    break;
            }
        } while (opcao != 0);
    }
}