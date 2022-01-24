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

function update_select_ajax(ajax_url, sel_id) {
    $.ajax({
        type: 'GET',
        url: ajax_url,
        success: function (response) {
            var c = ajax_url.charAt(19);
            if (c == 'p') {
                update_pessoa_select(response, sel_id);
            } else if (c == 'l') {
                update_localizacao_select(response, sel_id);
            }
        },
        error: function (response) {
            console.log("Error loading AJAX: " + response);
        }
    })
}

function update_pessoa_select(response, sel_id) {
    var sel = document.getElementById(sel_id);
    var index = sel.selectedIndex;
    while (sel.length > 1) {
        sel.remove(1);
    }
    
    var pessoas = JSON.parse(response["pessoas"]);
    
    var i;
    for(i = 0; i < pessoas.length; i++) {
        var fields = pessoas[i].fields;
        var opt = new Option(fields.nome + " - " + fields.cpf, pessoas[i].pk);
        sel.options.add(opt);
    }

    sel.selectedIndex = index;
}

function update_localizacao_select(response, sel_id) {
    var sel = document.getElementById(sel_id);
    var index = sel.selectedIndex;
    while (sel.length > 1) {
        sel.remove(1);
    }
    
    var localizacoes = JSON.parse(response["localizacoes"]);
    
    var i;
    for(i = 0; i < localizacoes.length; i++) {
        var fields = localizacoes[i].fields;
        var opt = new Option(fields.codigo + " - " + fields.coordenadas, localizacoes[i].pk);
        sel.options.add(opt);
    }

    sel.selectedIndex = index;
}