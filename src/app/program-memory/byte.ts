export class Byte{
    isValid:boolean
    Decimal: number;
    Binary:string;
    Hexadecimal: string

    constructor(){
        this.isValid=true
        this.Decimal = 0;
        this.Binary = '00000000'
        this.Hexadecimal = '000'
    }

}