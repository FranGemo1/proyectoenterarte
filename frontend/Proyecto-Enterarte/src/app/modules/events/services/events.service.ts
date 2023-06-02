import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Event } from '../interfaces/event';

@Injectable({
  providedIn: 'root'
})
export class EventsService {

  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type':'application/json'
    })
  }

  constructor(private httpClient: HttpClient ) { }

  private apiURL: string = 'http://localhost:3000/eventos/'

  getEvents () : Observable <Event[]> {
    return this.httpClient.get<Event[]>(this.apiURL);
  } 

  getEvent (id:number) : Observable <Event> {
    return this.httpClient.get<Event>(this.apiURL+id)
  }

  addEvent (event:Event) : Observable <Event> {
    return this.httpClient.post<Event>(this.apiURL,event,this.httpOptions)
  }
   

}
