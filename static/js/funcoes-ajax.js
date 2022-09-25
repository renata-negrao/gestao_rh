function utilizouHoraExtra(id){
    console.log(id);
    token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    valor = document.getElementById('campoX').value;

    console.log(valor);
    $.ajax({
        type: 'POST',
        url: '/horas-extras/utilizou-hora-extra/' + id + '/',
        data: {
            csrfmiddlewaretoken: token,
            outro_param: valor
        },
        success: function(result){
            console.log(result);
            $("#mensagem").text(result.mensagem);
            $("#horas_atualizadas").text(result.horas);
        }
    });
}

function naoutilizouHoraExtra(id){
    console.log(id);
    token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    valor = document.getElementById('campoX').value;

    console.log(valor);
    $.ajax({
        type: 'POST',
        url: '/horas-extras/nao-utilizou-hora-extra/' + id + '/',
        data: {
            csrfmiddlewaretoken: token,
            outro_param: valor
        },
        success: function(result){
            console.log(result);
            $("#mensagem").text(result.mensagem);
            $("#horas_atualizadas").text(result.horas);
        }
    });
}