$(document).ready(function () {
    $('.ajaxLoader').hide();
    $('.filter-checkbox,#priceFilterButton').on('click',function () {
        var _filterObj = {};
        var _minprice = $('#maxprice').attr('min');
		var _maxprice = $('#maxprice').val();
		_filterObj.minprice =_minprice;
		_filterObj.maxprice = _maxprice;
        $('.filter-checkbox').each(function (index,ele) {
            var _filterVal = $(this).val();
            // vat _filterKey=$(this).attr('data-filter');
            var _filterKey = $(this).data('filter')
            _filterObj[_filterKey]=Array.from(document.querySelectorAll('input[data-filter='+_filterKey+']:checked')).map(function(el){
			 	return el.value;
            });
        });
        console.log(_filterObj)
        // run ajax
        $.ajax({
			url:'/filter_products',
			// type:'GET',
			// url : "{% url 'filter_products' %}",
			data : _filterObj,
			dataType:'json',
			beforeSend : function(){
				// $('#filteredproducts').html('loading')
				$(".ajaxLoader").show();
			},
			success : function(res){
				console.log(res);
				$("#filteredproducts").html(res.data);
				$(".ajaxLoader").hide();
			}
		});
    });
//    ending ajax syntax
// 			price filter Jquiry Code
		$('#maxprice').on('blur',function () {
			var _min = $(this).attr('min');
			var _max = $(this).attr('max');
			var _value = $(this).val();
			console.log(_value,_min,_max)
			if (_value < parseInt(_min) || _value > parseInt(_max)) {
				alert('value should be '+_min+'-'+_max)
				$(this).val(_min);
				$(this).focus();
				$('#rangeinpur').val(_min);
				return false
			}

		});



});
