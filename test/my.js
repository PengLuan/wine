$(function(){
	let BaseUrl = "http://127.0.0.1:5000/chat";
	const UUID = crypto.randomUUID();
	$("#send").click(function(){
		let text = $("#text").val();
		if(text){
			$("#container").append("<div class='for-human'>" + text + "</div>")
			$.get(BaseUrl, {"text": text, "session_id": UUID}, function(res){
				if(res.code == 0){
					$("#container").append("<div class='for-robot'>" + res.data.text + "</div>");
				}
				console.log(res);
			});
		}else{
			alert("请输入聊天内容")
		}
	});
});