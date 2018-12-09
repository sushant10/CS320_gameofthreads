$(document).ready(function(){
	$('#systems-table').DataTable({
		scrollY:        400,
		scrollCollapse: true,
		paging:         true,
		serverSide: 	true,
		ajax: 		"dt/",
		"bSort": true,
		"bSearchable":true,	
		"order": 		[[ 0, "asc"]],
		"aoColumns": [
		{
			"mRender": function (data, type, row){
				return "<a href=" + row[0] + ">" + row[0] + "</a>";
			}
		},
		{},
		{
			"mRender": function (data, type, row){	
				var date = new Date(row[2]);
				var months = ["Jan.", "Feb.", "March", "April", "May", "June", "July", "Aug.", "Sept.", "Oct.", "Nov.", "Dec."];
				return months[date.getMonth()] + " " + (1 + date.getDate()) + ", " + date.getFullYear();
			}
		},
		{
			"mRender": function (data, type, row){
				return row[3] + "%";
			}
		}
		],
        "fnRowCallback": function( nRow, aData, iDisplayIndex, iDisplayIndexFull ) {
        		var capacity_string = aData[3];
				var capacity = capacity_string.substr(0, capacity_string.length - 1)/100.0;		
				capacity /= 0.3 
				if (capacity > 1){
					return;
				}
				var color = "rgba(" + 220 + ","
									+ 0 + "," 
									+ 0 + ","
									+ ((1-capacity)*0.5 + 0.2) + ")";
				$(nRow).children().last().css("background-color", color);
            },
		fixedColumns:   {
			heightMatch: 'none'
		}
	});
});

$(window).resize(function(){
	$('#systems-table').DataTable().draw();
});
