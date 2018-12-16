$(document).ready(function(){
	$('#files-table').DataTable({
		scrollY:        400,
		//scrollX:        true,
		scrollCollapse: true,
		paging:         false,
		fixedColumns:   {
			heightMatch: 'none'
		},
		order: 		[[ 0, "desc"]],
		columns: [
			{"type": "html"},
			{"type": "date"},
			{"type": "html", "searchable": false},
			{"type": "html", "searchable": false}
		]
	});
});

$(window).resize(function(){
	$('#files-table').DataTable().draw();
});
