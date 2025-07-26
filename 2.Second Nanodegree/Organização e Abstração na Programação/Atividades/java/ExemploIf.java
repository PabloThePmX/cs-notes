import java.util.Scanner;

public class ExemploIf {
    public static void main(String[] args) {
        Scanner lerTexto = new Scanner(System.in);
        System.out.print("Digite a primeira nota: ");
        double nota1 = lerTexto.nextDouble();
        lerTexto.nextLine();
        System.out.print("Digite a segunda nota: ");
        double nota2 = lerTexto.nextDouble();
        lerTexto.close();
        double mediaFinal = calculaNota(nota1, nota2);
        System.out.printf("A média final do aluno foi %.2f\n", mediaFinal);

        if(mediaFinal >= 7)
            System.out.println("Aprovado!");
        else if (mediaFinal >= 3)
            System.out.println("Exame!");
        else
            System.out.println("Reprovado!");
    }

    public static double calculaNota(double nota1, double nota2){
        return (nota1 + nota2)/2;
    }
}
