import java.util.Scanner;

public class EntradaDados {
    public static void main(String[] args) {
        Scanner lerTeclado = new Scanner(System.in);
        System.out.print("Digite seu nome: ");
        String nome = lerTeclado.nextLine();
        System.out.print("Digite a sua idade: ");
        int idade = lerTeclado.nextInt();
        //após valores númericos, invocar o método nextLine para limpar o buffer.
        lerTeclado.nextLine();
        System.out.println("Seu nome é " + nome + "e sua idade é " + idade);
        lerTeclado.close();
    }
}
