package GestaoBibliotecaFinal;

public class TestePolimorfismo {
    public static void main(String[] args) {
        Livro livro1 = new Livro();
        Livro livro2 = new LivroDigital();
        Livro livro3 = new LivroFisico();

        //vai depender do tipo concreto
        System.out.println(livro1.toString());
        System.out.println(livro2.toString());
        System.out.println(livro3.toString());
    }
}
