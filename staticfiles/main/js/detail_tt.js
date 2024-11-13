function warning_reload(tid){
    warning_reload = document.getElementById(`warning_reload_${tid}`);
    if (warning_reload.hasAttribute('hidden')){
        warning_reload.removeAttribute('hidden');
    }
}

function rename(ttid){
    inp = document.getElementById('tt_name_inp');

    fetch(`../rename/${ttid}`, {
        method: "POST",
        body: JSON.stringify({
          name: inp.value
        }),
        headers: {
          "Content-type": "application/json; charset=UTF-8"
        }
      });
}

function make_assign_button_active(tid){
    b = document.getElementById(`button_${tid}`)
    if (b.hasAttribute('disabled')){
        b.removeAttribute('disabled')
    }
    select = document.getElementById(`select_${tid}`)
    if (select.options[0].value == -1){
        select.remove(0)
    }
}

function make_create_task_button_active(){
    task_name = document.getElementById('task_name_input').value
    b = document.getElementById(`create_task_button`)
    if (task_name){
        if (b.hasAttribute('disabled')){
            b.removeAttribute('disabled')
        }
    }
    else{
        b.setAttribute('disabled', true)
    }

}

function assign_contributor(tid){
    cid = Number(document.getElementById(`select_${tid}`).value)
    fetch(`../assign_contributor`, {
        method: "POST",
        body: JSON.stringify({
          task_id: tid,
          user_id: cid
        }),
        headers: {
          "Content-type": "application/json; charset=UTF-8"
        }
      });
    statuses_div = document.getElementById(`status_bar_${tid}`)
    div_filling = ``
    warning_reload(tid);


}

function delete_task(tid){
    fetch(`../delete_task`, {
        method: "POST",
        body: JSON.stringify({
          task_id: tid,
        }),
        headers: {
          "Content-type": "application/json; charset=UTF-8"
        }
      });
      document.getElementById(`task_${tid}`).remove();
      
      
}

function mark_as_executed(tid){
    fetch(`../execute_task`, {
        method: "POST",
        body: JSON.stringify({
          task_id: tid,
        }),
        headers: {
          "Content-type": "application/json; charset=UTF-8"
        }
      });
      warning_reload(tid);

}

function mark_as_checked(tid){
    fetch(`../check_task`, {
        method: "POST",
        body: JSON.stringify({
          task_id: tid,
        }),
        headers: {
          "Content-type": "application/json; charset=UTF-8"
        }
      });
      warning_reload(tid);

}

function edit_desc(tid){
    text = document.getElementById(`desc_text_${tid}`).value
    console.log(text)
    fetch(`../edit_desc`, {
        method: "POST",
        body: JSON.stringify({
          task_id: tid,
          text: text
        }),
        headers: {
          "Content-type": "application/json; charset=UTF-8"
        }
      });
}

