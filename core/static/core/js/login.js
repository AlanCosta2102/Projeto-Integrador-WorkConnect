const input = document.getElementById('identificacao');

if (input){
    input.addEventListener('input',() => {
    let value = input.value.replace(/\D/g,'');

    if (value.length <=11){
      value = value.replace(/(\d{3})(\d)/, '$1.$2');
      value = value.replace(/(\d{3})(\d)/, '$1.$2');
      value = value.replace(/(\d{3})(\d{1,2})$/, '$1-$2'); 
    
}else{
      value = value.replace(/^(\d{2})(\d)/, '$1.$2');
      value = value.replace(/^(\d{2})\.(\d{3})(\d)/, '$1.$2.$3');
      value = value.replace(/\.(\d{3})(\d)/, '.$1/$2');
      value = value.replace(/(\d{4})(\d)/, '$1-$2');
}

  input.value = value;

});

}

function validarCPF(cpf){
    cpf = cpf.replace(/\D/g,'');
    if (cpf.length !== 11 || /^(d)\1+$/.test(cpf)) return false;

    let soma = 0;
    for (let i=0;i<9;i++) soma += cpf[i] * (10-i);
    let dig1 = (soma *10) % 11;
    dig1 = dig1 == 10 ? 0: dig1;
    if (dig1 != cpf[9]) return false;

    soma = 0;
    for(let i = 0;i<10;i++) soma += cpf[i] * (11 - i);
    let dig2 = (soma * 10) % 11;
    dig2 = dig2 == 10 ? 0: dig1;
    return dig2 == cpf[10];
}

function validarCNPJ(cnpj){
    cnpj = cnpj.replace(/\D/g, '');
    if (cnpj.length !== 14 || /^(\d)\1+$/.test(cnpj)) return false

    const pesos1 = [5,4,3,2,9,8,7,6,5,4,3,2];
    const pesos2 = [6].concat(pesos1);

    const calc = (base,pesos) => {
        let soma = 0;
        for (let i = 0;i<pesos.length;i++){
            soma += base[i] * pesos[i];
        }
        let resto = soma % 11;
        return resto < 2 ? 0: 11 - resto;
    };
    
    const dig1  = calc(cnpj,pesos1);
    const dig2 = calc(cnpj,pesos2);

    return dig1 == cnpj[12] && dig2 == cnpj[13];
}

function validarIdentificacao(){
    const idt = document.getElementById('identificacao').value;
    const limpo = idt.replace(/\D/g, '');

    if(limpo.length === 11 && !validarIdentificacao(limpo)){
        alert('CPF invalido.');
        return false;
    }

    if (limpo.length === 14 && !validarCNPJ(limpo)){
        alert('CNPJ inválido.');
        return false;
    }

    if (limpo.length !== 11 && limpo.length !== 14){
        alert('Digite um CPF ou CNPJ válido.');
        return false;
        
    }
    return true;
}
document.querySelector('.toggle-btn').onclick = () => {
  document.querySelector('.sidebar').classList.toggle('open');
};
