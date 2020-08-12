//Author: Jack Clarke
//class that would get information from the raspberry pi
//methods aren't asynchronous now, but they will be soon
//TODO: Make music and light State machine
import isReachable from "is-reachable";
interface data {
  data: string;
}
export default class RaspberryPi {
  ip: string;
  port: number;
  musicPlaying: boolean; // not implemented yet
  url: string;
  constructor(ip: string, port: number) {
    this.ip = ip;
    this.port = port;
    this.musicPlaying = false; //not implemented yet
    this.url = "http://"+ip + ":" + port;
    
  }

  setPort(newPort: number): boolean {
    this.port = newPort;
    return true;
  }
  getPort(): number {
    return this.port;
  }

  isUp(): boolean {
    let piisup: boolean;
    try {
      const response = fetch(this.url + "/temp");
      piisup = true;
      return true;
    } catch (e) {
      piisup = false;
      return false;
    }
  }
  //gets room temp
  async getTemp(): Promise<number> {
    const myJson = await this.getData("/temp");
    const temp = <number>myJson.data;
    return temp;
  }
  async getLight(): Promise<number> {
    const myJson = await this.getData("/brightness");
    const temp = <number>myJson.data;
    return temp;
  }
  async getHumidity(): Promise<number> {
    const myJson = await this.getData("/humidity");
    const temp = <number>myJson.data;
    return temp;
  }
  async doorOpen(): Promise<boolean> {
    const myJson = await this.getData("/door");
    const temp = <boolean>myJson.data;
    return temp;
  }
  
  async getAllSensorData(): Promise<Record<string, unknown>> {
    let myJson = this.getData("/all")
    return myJson;
  }
  // Receives data from a route in the rasppi server, and returns it as json. Returns an error if something goes wrong
  async getData(route: string): Promise<Record<string, unknown>> {
    try {
      const response = await fetch(this.url + route);
      const myJson: Record<string, unknown> = await response.json();
      return myJson;
    } catch (e) {
      console.log(e);
      return { data: "ServerError, is your server up?"};
    }
  }
}

export interface mood {
  Song: string;
  LightColor: string;
  LightStrength: number;
}
