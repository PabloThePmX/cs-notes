public class Veiculo {
    //atributos
    private String placa;
    private int ano;
    private String marca;
    
    public Veiculo() {
    }
    
    public String getPlaca() {
        return placa;
    }

    public void setPlaca(String placa) {
        this.placa = placa;
    }

    public int getAno() {
        return ano;
    }

    public void setAno(int ano) {
        this.ano = ano;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public Veiculo(String placa, int ano) {
        this.placa = placa;
        this.ano = ano;
    }

    public Veiculo cloneMe(){
        //clonar as prop nesse novo veiculo e mandar de volta
        return new Veiculo();
    }
}