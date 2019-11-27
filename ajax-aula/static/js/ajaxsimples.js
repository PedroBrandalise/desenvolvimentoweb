function onMouseOver(texto){
	texto.style.color = "red";

}
function onMouseOut(texto){
	texto.style.color = "black";
}


$(function(){
	$('button').click(function(){
		var user = $('#inputUsername').val();
		var pass = $('#inputPassword').val();
		$.ajax({
			url: '/pessoas',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
				console.log(response.pessoas);
				console.log(response.pessoas[0]);
				document.getElementById("primeiro").innerHTML = response.pessoas[0].nome;
				document.getElementById("segundo").innerHTML = response.pessoas[1].nome;

				var list = document.createElement('ul');

				for (i = 0; i < response.pessoas.length; i++){
					var item = document.createElement('li'); 
					item.appendChild(document.createTextNode(response.pessoas[i].nome));
					list.appendChild(item);
				}

				document.getElementById('segundo').appendChild(list);

				var tabela = document.getElementById("listagem");
				console.log(tabela);

				for (i = 0; i < response.pessoas.length; i++){
					var tr = document.createElement('tr');
					var td = document.createElement('td');
					td.innerHTML = response.pessoas[i].nome;
					tr.scope = "row";
					tr.appendChild(td);
					tabela.appendChild(tr);
				}
				document.getElementById('listagem').style.display="table";
				document.getElementById('listagem').style.margin ="auto";
				
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});
