function somaIntervalo(array, num = 1) {
    const result = [];

    for(let i = 0; i < array.length; i++) {
        result.push(array[i] ** num);
    }

    return result
}

somaIntervalo([1, 2, 3, 4], 2)




function sum(x, y, z) {
    return x + y + z;
}
const numbers = [1, 2, 3];

sum(...numbers);




function confereTamanho(...args) {
    //console.log(args.length)
}

confereTamanho()
confereTamanho(1, 2)
confereTamanho(3, 4, 5)



function numeroPositivo(num) {

    const ehNegativo = num < 0;
    const maiorQueDez = num > 10;

    if(ehNegativo) {
        return "Esse número é nnegativo!";
    } else if (!ehNegativo && maiorQueDez) {
        return "Esse número é positivo e maior que 10!"
    }

    return "Esse número é positivo!"
}

numeroPositivo(-9)




function exemploWhile() {
    let num = 0

    while(num <= 5) {
        console.log(num);
        num++;
    }
}
exemploWhile()