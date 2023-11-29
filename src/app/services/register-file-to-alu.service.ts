import { Injectable } from '@angular/core';
import { register } from '../register-file/register';

@Injectable({
  providedIn: 'root'
})
export class RegisterFileToALUService {

  constructor() { }

  ReadData1: register = new register()
  ReadData2: register = new register()
  ResultFromALU: register = new register()

}
