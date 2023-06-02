import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { EventsService } from '../../services/events.service';
import { Event } from '../../interfaces/event';

@Component({
  selector: 'app-event-item',
  templateUrl: './event-item.component.html',
  styleUrls: ['./event-item.component.css']
})
export class EventItemComponent implements OnInit{

  event!: Event;

  constructor (private route: ActivatedRoute,
               private eventService: EventsService) {}
  
  ngOnInit () {

 
    this.route.params.subscribe(params => {        
        this.eventService.getEvent(params['id']).subscribe(data => {
          this.event = data
         
        });

    })  
   
    
  }
}
