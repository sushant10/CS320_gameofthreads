$(document).ready(function(){
	$('#files-table').DataTable({
		scrollY:        400,
		//scrollX:        true,
		scrollCollapse: true,
		paging:         false,
		fixedColumns:   {
			heightMatch: 'none'
		}
	});
});