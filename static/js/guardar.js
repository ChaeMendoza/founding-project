const guardarSolCapmania=(pnombre,descripcion,categori_id,beneficiario,csrf_token,monto_x_recaudar,email)=>{
    const solCampania={
        nombre:pnombre,
        descripcion:descripcion,
        categorias:categori_id,
        beneficiario:beneficiario,
        monto_x_recaudar:monto_x_recaudar,
        email:email
    }
    if(
        pnombre == '' ||
        descripcion == '' ||
        categori_id == '' ||
        beneficiario == '' ||
        monto_x_recaudar == '' ||
        monto_x_recaudar == '0' ||
        email == ''
    ) {
        Swal.fire({
            html: "<span style='color: white;'>Debe llenar todos los campos.</span>",
            icon: "info"
        });
        return;
    }
    fetch('/guardar/solCampania/',{
        method:'POST',
        body:JSON.stringify(solCampania),
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrf_token
        }
    })
    .then(res => res.json())
    .then(data => Swal.fire({
            html: "<span style='color: white;'>Campaña guardada con éxito.</span>",
            icon: "success",
            allowOutsideClick: false
        }).then((result) => {
            if (result.isConfirmed) {
                location.reload()
            }
        })
    )
    .catch(error => Swal.fire({
            html: "<span style='color: white;'>No se pudo guardar la campaña.</span>",
            icon: "error"
        }) 
    );
    return false;
}