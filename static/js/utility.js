$(function (){

	

$('.carter').click(function(){
	
	var itemNum = $('.itemNum').text();
	var itemNum2 = $('.itemNum2').text();
	var itemPrice = $('#itemPrice').text();
	var curr_price = $(this).val();


	itemNum = parseInt(itemNum);
	itemNum += 1;
	itemNum2 = parseInt(itemNum2);
	itemNum2 += 1;
	itemPrice = parseInt(itemPrice);
	curr_price = parseInt(curr_price);


	itemPrice += curr_price;
	$('#num_of_items').text(itemNum);
	$('.itemNum2').text(itemNum2);
	$('#itemPrice').text(itemPrice);
	$(this).text("REMOVE ITEM");
	$(this).toggleClass('uncart');
	$(this).toggleClass('uncart');

	$(this).attr("disabled", "disabled");
})

	


$('.uncart').click(function(){

	var itemNum = $('.num_of_items').text();
	var itemNum2 = $('.itemNum2').text();
	var itemPrice = $('#itemPrice').text();
	var curr_price = $(this).val();


	itemNum = parseInt(itemNum);
	itemNum -= 1;
	itemNum2 = parseInt(itemNum2);
	itemNum2 -= 1;
	itemPrice = parseInt(itemPrice);
	curr_price = parseInt(curr_price);

	itemPrice -= curr_price;
	$('#num_of_items').text(itemNum);
	$('.itemNum2').text(itemNum2);
	$('#itemPrice').text(itemPrice);
	
	$(this).toggleClass('carter');
	$(this).text("ADD TO CART");

})



})

/*

item = $(this).closest(div).find(.productName).text();
	price = curr_price;
	$.ajax({
			type: 'POST',							
			url: '/keep_cart', 
			data: { item: item, price: price },
			dataType: 'json',
			success: function(data){
			}
		});


*/


