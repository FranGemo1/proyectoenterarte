import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { HttpClient } from '@angular/common/http';

declare var paypal;

@Component({
  selector: 'app-fdepagos',
  templateUrl: './fdepagos.component.html',
  styleUrls: ['./fdepagos.component.css']
})
export class FdepagosComponent implements OnInit {
  @ViewChild('paypal', {static:true}) paypalElement: ElementRef;
  producto: any;

  constructor(private http: HttpClient) { }

  ngOnInit() {
    this.obtenerDetallesProducto(); 

    paypal
      .Buttons({
        createOrder: (data, actions) => {
          return actions.order.create({
            purchase_units: [
              {
                description: this.producto.description,
                amount: {
                  value: this.producto.precio
                }
              }
            ]
          });
        },
        onApprove: async (data, action) => {
          const order = await action.order.capture();
          console.log(order);
        },
        onError: err => {
          console.log(err);
        }
      })
      .render(this.paypalElement.nativeElement);
  }

  obtenerDetallesProducto() {
    const url = 'http://localhost:8000/api/v1/payment/checkout'; 

    this.http.get(url)
      .subscribe(
        (response: any) => {
          this.producto = response;
        },
        (error) => {
          console.log(error);
        }
      );
  }
}
