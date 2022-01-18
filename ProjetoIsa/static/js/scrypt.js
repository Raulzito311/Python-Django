let pessoaFormWindow;
let localizacaoFormWindow;

function open_pessoa_form() {
    pessoaFormWindow = window.open('/questionario/pessoa', '', 'width=600,height=500');
}

function close_pessoa_form() {
    pessoaFormWindow.close();
}

function open_localizacao_form() {
    localizacaoFormWindow = window.open('/questionario/localizacao', '', 'width=600,height=500');
}

function close_localizacao_form() {
    localizacaoFormWindow.close();
}

function close_win() {
    window.close();
}