package GestaoBibliotecaFinal;

public class LivroFisico extends Livro {
    private int nExemplares;
    private String dimensoes;

    public int getnExemplares() {
        return nExemplares;
    }
    public void setnExemplares(int nExemplares) {
        this.nExemplares = nExemplares;
    }
    public String getDimensoes() {
        return dimensoes;
    }
    public void setDimensoes(String dimensoes) {
        this.dimensoes = dimensoes;
    }

    @Override
    public String toString(){
        return "Livro Físico: " + "Título " + getTitulo() + " - Autor: " + getAutor() + "- Ano: " + getAnoPublicacao() + "Dimensões: " + getDimensoes();
    }
}
