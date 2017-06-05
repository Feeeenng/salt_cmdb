/**
 * Created by FenG on 2017/5/26.
 */

function getHosts() {
    $.ajax({
        url:'hosts/get/all',
        success:function (res) {
            console.log(res)
            var body = res.data.content
            for (var i = 0, len = body.length, htmls = [],hosts = []; i < len; i++) {

                htmls.push([
                    '<tr>',
                        '<td><input type="checkbox" name="" lay-skin="primary"></td>',
                        '<td>', body[i].server_id ,'</td>',
                        '<td>',body[i].name,'</td>',
                        '<td>',body[i].host,'</td>',
                        '<td>',body[i].eth0,'</td>',
                        '<td>',body[i].eth1,'</td>',
                      '</tr>'
                ].join(''));

                hosts.push([
                    '<option value="',body[i].name,'" id="option_name">',body[i].name ,'</option>'
                ].join(''));

            }
            $('#host').html(htmls.join(''));
            $('#host_all').html(hosts.join(''))

        }

})
}
getHosts()

$('#zhixing').click(function () {
    var data = {
        'tgt': $('#host_all').val(),
        // 'fun':$('#run').val(),
        'arg':$('#run').val()
    }
    console.log(data)
    $.ajax({
        type:'POST',
        url:'hosts/server',
        data:JSON.stringify(data),
        success:function (res) {

            $('#run_result').html(res.data.return[0][$('#host_all').val()].replace(/\n/g, '<br>'))

        }

    })
})


