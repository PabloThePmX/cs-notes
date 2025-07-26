import java.util.Scanner;

public class ClassificacaoImc {
    public static void main(String[] args) {
        Scanner lerTexto = new Scanner(System.in);
        System.out.print("Gênero: ");
        char genero = Character.toUpperCase(lerTexto.next().charAt(0));
        lerTexto.nextLine();
        System.out.print("Altura: ");
        double altura = lerTexto.nextDouble();
        lerTexto.nextLine();
        System.out.print("Peso: ");
        double peso = lerTexto.nextDouble();
        lerTexto.nextLine();
        lerTexto.close();

        double valorIMC = calculoImc(peso, altura);

        if(genero == 'M'){
            if(valorIMC >= 40)
                mensagens("OB_Mor");
            else if(valorIMC >= 30)
                mensagens("OB_Mod");
            else if(valorIMC >= 25)
                mensagens("OB_Lev");
            else if(valorIMC >= 20)
                mensagens("Norm");
            else
                mensagens("Ab_Norm");
        } else{
            if(valorIMC >= 39)
                mensagens("OB_Mor");
            else if(valorIMC >= 29)
                mensagens("OB_Mod");
            else if(valorIMC >= 24)
                mensagens("OB_Lev");
            else if(valorIMC >= 19)
                mensagens("Norm");
            else
                mensagens("Ab_Norm");
        }
    }
    
    public static double calculoImc(double peso, double altura){
        return peso / (Math.pow(altura, 2));
    }

    public static void mensagens(String tipo){

        if(tipo.equals("OB_Mor"))
            System.out.println("Obesidade Mórbida");
        
        if(tipo.equals("OB_Mod"))
            System.out.println("Obesidade Moderada");
        
        if (tipo.equals("OB_Lev"))
            System.out.println("Obesidade Leve");
        
        if(tipo.equals("Norm"))
            System.out.println("Normal");
        
        if(tipo.equals("Ab_Norm"))
            System.out.println("Abaixo do Normal");
    }
}