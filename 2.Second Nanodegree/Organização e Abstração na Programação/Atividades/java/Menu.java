import java.util.Scanner;

public class Menu {
    public static void main(String[] args) {
        Scanner lerTexto = new Scanner(System.in);
        int opcao;
        do{
            String menu = """
                    Escolha uma das opções:
                    1 - Cadastrar
                    2 - Excluir
                    0 - Sair
                    """;
            System.out.println(menu);
            opcao = lerTexto.nextInt();
            lerTexto.nextLine(); //limpa buffer
        } while(opcao != 0);
        lerTexto.close();
    }
}
