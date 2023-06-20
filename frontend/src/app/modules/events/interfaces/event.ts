export interface Event {
       
        id:number,
        name:string,
        price:number,
        date?:Date,
        day?:string,
        img:string,
        category:string,
        gender: string,
        province:string,
        city:string,
        street:string,
        number:string,
        social_networks: {
            instagram?: string,
            facebook?: string,
            website?: string
        },
        description:string    
}