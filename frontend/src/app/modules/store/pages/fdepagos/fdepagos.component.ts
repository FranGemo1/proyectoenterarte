import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';

declare var paypal;

@Component({
  selector: 'app-fdepagos',
  templateUrl: './fdepagos.component.html',
  styleUrls: ['./fdepagos.component.css']
})
export class FdepagosComponent implements OnInit{
  @ViewChild('paypal', {static:true}) paypalElement : ElementRef;

  producto = {
    description: "Taller de Musica",
    precio: 250,
    img: "Img"
  }


  ngOnInit(){

    paypal
    .Buttons({
      createOrder:(data, actions) => {
        return actions.order.create({
          purchase_units:[
            {
              description: this.producto.description,
              amount : {

                value: this.producto.precio
              }
            }
          ]
        })
      },
      onApprove: async (data, action)=>{
        const order = await action.order.capture();
        console.log(order);
      },
      onError: err=>{
        console.log(err);
      }
    })
    .render(this.paypalElement.nativeElement);
  }
}
