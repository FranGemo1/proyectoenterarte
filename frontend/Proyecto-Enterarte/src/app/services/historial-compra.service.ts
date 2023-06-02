import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class HistorialCompraService {

  constructor(private http: HttpClient) { }

  baseEndPoint: string = "http://localhost:3000/response";

  mostrarHistorial(): Observable <any>{
    return this.http.get <any>(this.baseEndPoint);

  }
}
