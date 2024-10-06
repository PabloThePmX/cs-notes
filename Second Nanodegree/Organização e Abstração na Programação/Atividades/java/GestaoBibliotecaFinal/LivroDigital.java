package GestaoBibliotecaFinal;

public class LivroDigital extends Livro {
    private double tamanhoArquivo;
    private String formatoArquivo;

    public double getTamanhoArquivo() {
        return tamanhoArquivo;
    }
    public void setTamanhoArquivo(double tamanhoArquivo) {
        this.tamanhoArquivo = tamanhoArquivo;
    }
    public String getFormatoArquivo() {
        return formatoArquivo;
    }
    public void setFormatoArquivo(String formatoArquivo) {
        this.formatoArquivo = formatoArquivo;
    }

    @Override
    public String toString(){
        return "Livro Digital: " + "Título " + getTitulo() + " - Autor: " + getAutor() + "- Ano: " + getAnoPublicacao() + "Formato: " + getFormatoArquivo();
    }
}
