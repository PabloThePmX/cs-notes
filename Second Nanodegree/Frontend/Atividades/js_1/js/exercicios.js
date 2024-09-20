//ex1
let nome = "pablo"

//ex2
let qtd = 10
let preco = 12.99

//ex3
let valorTotal = qtd*preco

//ex4
let idade = 24
let frase = `Olá, me chamo ${nome} e minha idade é ${idade} anos`

//ex5
let naoDefinido

//ex6
let nulo = null

//ex7
let valorProduto = "6000"
let imposto = "750"

//ex8
let nomeProduto = "S21 Ultra"
let valorUni = 4000
let qtdProduto = 5
let totalProdutos = valorUni*qtdProduto
let fraseEx8 = `Produto ${nomeProduto} valor unitário R$${valorUni} e valor total R$${totalProdutos}`

//ex9
function criaFraseValores(nomeProdutoFunction, valorUniFunction, qtdFunction){
    let totalProdutos = valorUniFunction*qtdFunction
    return fraseEx9 = `Produto ${nomeProdutoFunction} valor unitário R$${valorUni} e valor total R$${totalProdutos}`
}

//ex10
function isPositiveOrNegative(numero){
    // return numero > 0 
    // ? "positivo" 
    // : numero == 0 
    //     ? "neutro" 
    //     : "negativo"
    if(numero > 0)
        return "positivo"

    if(numero < 0)
        return "negativo"

    return "neutro"
}

console.log(isPositiveOrNegative(2))