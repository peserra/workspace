
function tocaSomPom(){
    document.querySelector('#som_tecla_pom').play();
}
function tocaSomClap(){
    document.querySelector('#som_tecla_clap').play();
}

/*
document.querySelector('.tecla_pom').onclick = tocaSomPom; // pega referencia mas nao executa de uma vez
document.querySelector('.tecla_clap').onclick = tocaSomClap;*/

// para selecionar todos os botoes desejados de uma vez
// guardar numa constante
const listaDeTeclas = document.querySelectorAll('.tecla');


