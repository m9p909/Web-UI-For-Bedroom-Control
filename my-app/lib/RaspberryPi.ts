export default class RaspberryPi {
  ip: string;
  port: number;
  constructor(ip: string, port: number) {
    this.ip = ip;
    this.port = port;
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
