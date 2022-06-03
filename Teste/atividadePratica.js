const alunos = [
{
    nome: 'Marcos',
    nota: 7,
    turma: '3B'
},
{
    nome: 'Aila',
    nota: 4,
    turma: '2B'
},
{
    nome: 'Sofia',
    nota: 9,
    turma: '1B'
}
]

function alunosAprovados(arr, media){
    let aprovados = [];
    
    for(let i = 0; i < arr.length; i++) {
        const {nota, nome} = arr[i];

        if(nota >= media) {
            aprovados.push(nome);
        }
    }
    return aprovados;
}

alunosAprovados(alunos, 5)




function calculaIdade(anos)  {
    return `Daqui a ${anos} anos, ${this.nome} terá ${
        this.idade + anos
    } anos de idade.`;
}

const pessoa1 = {
    nome: "Maria",
    idade: 15
}
const pessoa2 = {
    nome: "Carla",
    idade: 13
}
const pessoa3 = {
    nome: "Ana",
    idade: 11
}

calculaIdade.call(pessoa2, 11);




async function resolvePromise(){
    const myPromise = new Promise((resolve, reject) => {
        window.setTimeout(() => {
            resolve('Resolvida');
        }, 3000);
});

const resolved = await myPromise
    .then((result) => result + ' passando pelo then')
    .then((result) => result + ' e agora acabou!')
    .catch((err) => console.log(err.message));

return resolved;

}