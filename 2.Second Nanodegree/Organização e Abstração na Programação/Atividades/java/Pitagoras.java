import java.util.Scanner;

public class Pitagoras {
    public static void main(String[] args) {
        //define que a entrada é do terminal
        Scanner lerTexto = new Scanner(System.in);
        System.out.print("Digite o cateto A: ");
        double catetoA = lerTexto.nextDouble();
        lerTexto.nextLine();
        System.out.print("Digite o cateto B: ");
        double catetoB = lerTexto.nextDouble();
        lerTexto.nextLine();
        lerTexto.close();

        double hipotenusa = calculaHipotenusa(catetoA, catetoB);
        System.out.println("A hipotenusa é " + hipotenusa);
    }

    public static double calculaHipotenusa(double a, double b){
        return Math.sqrt(Math.pow(a, 2) + Math.pow(b, 2));
    }
}
