import { Component, OnInit } from '@angular/core';
import { EventsService } from '../../services/events.service';
import { Event } from '../../interfaces/event';


@Component({
  selector: 'app-events',
  templateUrl: './events.component.html',
  styleUrls: ['./events.component.css']
})
export class EventsComponent implements OnInit {

  events!: Event[];

  mensual: string = "mensual"

  constructor (private eventsService : EventsService) {

  }
  
  ngOnInit(): void {
    this.eventsService.getEvents().subscribe(data => {
      this.events=data
    })
  }

  showAllEvents () {
    this.eventsService.getEvents().subscribe(data => {
      this.events=data
    })
  }

  filterEvents (gender:string) {

    this.eventsService.getEvents().subscribe(data => {
      this.events=data.filter(event => 
        event.gender==gender)
    })


  }



}
