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
    this.url = ip + ":" + port;
  }

  setPort(newPort: number): boolean {
    this.port = newPort;
    return true;
  }
  getPort(): number {
    return this.port;
  }

  async isUp(): Promise<boolean> {
    return await isReachable(this.url);
  }
  //gets room temp
  async getTemp(): Promise<number> {
    const response = await fetch(this.url + "/temp");

    const myJson = await response.json();
    const temp = <number>myJson.temp;
    return temp;
  }
  async getLight(): Promise<number> {
    const response = await fetch(this.url + "/brightness");
    const myJson = await response.json();
    const temp = <number>myJson.brightness;
    return temp;
  }
  async getHumidity(): Promise<number> {
    const response = await fetch(this.url + "/humidity");
    const myJson = await response.json();
    const temp = <number>myJson.humidity;
    return temp;
  }
  async doorOpen(): Promise<boolean> {
    const response = await fetch(this.url + "/door");
    const myJson = await response.json();
    const temp = <boolean>myJson.doorIsOpen;
    return temp;
  }
}

export interface mood {
  Song: string;
  LightColor: string;
  LightStrength: number;
}
