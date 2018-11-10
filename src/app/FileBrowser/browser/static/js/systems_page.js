$(document).ready(function(){
	$('#systems-table').DataTable({
		scrollY:        400,
		scrollCollapse: true,
		paging:         false,
		"order": 		[[ 0, "asc"]], 
		fixedColumns:   {
			heightMatch: 'none'
		}
	});
});

$(window).resize(function(){
	$('#systems-table').DataTable().draw();
});
