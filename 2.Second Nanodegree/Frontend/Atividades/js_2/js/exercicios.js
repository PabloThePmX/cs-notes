//ex1
const valores = [1,2,3,4,5]
let valorFinal = 0
for(let i = 0; i < valores.length; i++){
    valorFinal += valores[i]
}

//ex2
const numeros = [10,5,8,20,3]
let maiorValor = numeros[0] //or maiorValor = -Infinity //pega o primeiro valor pois deixar com 0, pode dar problema caso for um array de números negativos
for(let i = 0; i < numeros.length; i++){
    if(numeros[i] > maiorValor){
        maiorValor = numeros[i]
    }
}

//ex3
const numerosDup = [1,2,2,3,3,4,5,5]
let arrayAux = []
for(let i = 0; i < numerosDup.length; i++){
    if (!arrayAux.includes(numerosDup[i])){
        arrayAux.push(numerosDup[i])
    }
}

console.log(arrayAux.length)