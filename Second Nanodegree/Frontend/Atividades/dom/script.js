//escutar o evento de submit do botao de cep
const frmCep = document.getElementById("frmCep");
const cepInput = document.getElementById("cepInput");
const retornoDiv = document.getElementById("retorno"); 

frmCep.addEventListener("submit", function(event){
    event.preventDefault();
    const cep = cepInput.value;
    const retorno = fetch(`https://viacep.com.br/ws/${cep}/json/`);
    retorno.then(function(response){
        return response.json();
    }).then(function({logradouro, bairro, localidade, uf}){
        const endereco = `${logradouro}, ${bairro}, ${localidade} - ${uf}`
        retornoDiv.innerText = endereco;
    });    
});