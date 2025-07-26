import java.util.Random;
import java.util.Scanner;

public class JogoAdivinhacao {
    public static void main(String[] args) {
        try {
            while(true){
                String opcao = jogo();
                if (opcao.equals("0"))
                    break;
            }       
        } catch(Exception e){
            System.out.println("Valor inválido, reiniciando jogo...");
            main(args);
        }   
    }

    public static String jogo(){
        //#region declarando valores iniciais
        Random geradorAleatorio = new Random();
        int numeroAleatorio = geradorAleatorio.nextInt(0, 101);
        Scanner lerTexto = new Scanner(System.in);
        int qtdTentativas = 0;

        while (qtdTentativas <= 0) {
            System.out.print("\nDigite quantas tentativas você deseja... Lembrando, quanto menos, maior o desafio! - ");
            qtdTentativas = lerTexto.nextInt();
            lerTexto.nextLine();
        }
        //#endregion
    
        int qtdJogadas = 0;
        do {
            int numeroDigitado = 0;
            while (numeroDigitado <= 0 || numeroDigitado > 100) {
                System.out.print("Digite o número (maior que 0 e menor que 100): ");
                numeroDigitado = lerTexto.nextInt(); 
                lerTexto.nextLine();
            }
             
            qtdJogadas++;

            if(numeroDigitado == numeroAleatorio){
                System.out.printf("\nParabéns, o número era %s! Você precisou de %s tentativas para adivinha-lo!\n", numeroAleatorio, qtdJogadas);
                lerTexto.close();
                return "0";
            }
            else if (numeroAleatorio > numeroDigitado)
                System.out.println("O número é maior!");
            else
                System.out.println("O número é menor!");
            
            qtdTentativas--;

        } while(qtdTentativas > 0);  

        return gameOver(lerTexto);
    }

    public static String gameOver(Scanner lerTexto){
        System.out.println("Infelizmente não foi dessa vez! Digite qualquer tecla para recomeçar, ou 0 para sair!");
        return lerTexto.nextLine();
    }
}
