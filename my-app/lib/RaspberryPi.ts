//class that would get information from the raspberry pi
//methods aren't asynchronous now, but they will be soon
//TODO: Make music and light State machine

export default class RaspberryPi {
  ip: string;
  port: number;
  musicPlaying: boolean; // not implemented yet

  constructor(ip: string, port: number) {
    this.ip = ip;
    this.port = port;
    this.musicPlaying = false; //not implemented yet
  }

  setPort(newPort: number): boolean {
    return true;
  }
  getPort(): number {
    return this.port;
  }
  //gets room temp
  getTemp(): number {
    return 23;
  }
  getLight(): number {
    return 23;
  }
  getHumidity(): number {
    return 23;
  }
  getRoomEmpty(): boolean {
    return true;
  }
}

export interface mood {
  Song: string;
  LightColor: string;
  LightStrength: number;
}
