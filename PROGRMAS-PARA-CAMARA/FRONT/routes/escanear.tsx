import { FreshContext, Handlers,PageProps } from "$fresh/server.ts";
import { get_html_content } from "../scrap/scrap.tsx";


type ResponseData = {
    resultado: {
        carta:{
            image_uris:{
                normal: string;
            },
            prices: {
                usd: string;
                eur: string;
            },
            name: string;
        }
        
    }
}

type Carta_Recomendaciones = {
    resultado: {
        carta: {
            name: string;
            mana_cost: string;
            image_uris: {
                normal: string;
            }
            prices: {
                usd: string;
                usd_foil: string;
                usd_etched: string;
                eur: string;
                eur_foil: string;
                eur_etched: string;
            },
            purchase_uris: {
                cardmarket: string;
                tcgplayer: string;
            },
            oracle_text: string;
        },
        recomendaciones: [
            {
                name: string;
                image_uris: {
                    normal: string;
                }
            }
        ]
    }
}

type Carta_Recomendaciones_precio = {
    Carta_Recomendaciones : Carta_Recomendaciones;
    precios: string [];
}

export const handler:Handlers = {
    GET:async (req:Request,ctx:FreshContext<unknown,Carta_Recomendaciones>) => {
        const response = await fetch("http://localhost:8001/escanear_carta", {
            method: "POST",
        });
        if (!response.ok) {
            console.log("Error al escanear la carta", "error");
            console.error("Error al escanear la carta:", response.statusText);
            return ctx.render("");
        }
        
        const data:Carta_Recomendaciones = await response.json();
       console.log("Data recibida del backend:", data.resultado.carta.purchase_uris.cardmarket);
       const precios:string[] = await get_html_content(data.resultado.carta.purchase_uris.cardmarket);
       
      
              
        if (!data.resultado) {
            console.log("Error al escanear la carta", "error");
            console.error("Error al escanear la carta 2 :", response.statusText);
            return ctx.render(""); 
        }
        const resultado:Carta_Recomendaciones_precio = {
                Carta_Recomendaciones:data,
                precios: precios
        }
        return ctx.render(resultado);
        // console.log(data.resultado);
    }
   

}

const Page = (props:PageProps<Carta_Recomendaciones_precio>) => {
    console.log("Props recibidos en el componente:", props.data.Carta_Recomendaciones.resultado.carta.mana_cost.replace(/[{}]/g,"").trim());
    return (
        <div>
            <form method="GET" action="/escanear">
                <button type="submit">Escanear carta</button>
            </form>  
                      
            {props.data === "" ? <p>No se ha podido escanear la carta</p> :
                <div class ="carta-resultado">
                    <div>
                        <img src={props.data.Carta_Recomendaciones.resultado.carta.image_uris.normal} alt="Carta escaneada" />
                    </div>
                    <div>
                        <h2>Name: 
                            {
                                props.data.Carta_Recomendaciones.resultado.carta.name                            
                            }
                        </h2>
                        <div style={{ display: 'flex', alignItems: 'center' }}>
                            <h2>Mana Cost:</h2> {
                                   props.data.Carta_Recomendaciones.resultado.carta.mana_cost
                                        .match(/\{(.*?)\}/g)
                                        ?.map((mana: string, index: number) => {

                                            const symbol = mana.replace(/[{}]/g, "");

                                            if (symbol === "W") {
                                            return <img key={index} style={{ width: '50px', height: '20px' }} src="/colores/blanco.png" alt="White Mana" class="mana-symbol" />;
                                            }

                                            if (symbol === "U") {
                                            return <img key={index} style={{ width: '50px', height: '20px' }} src="/colores/azul.png" alt="Blue Mana" class="mana-symbol" />;
                                            }

                                            if (symbol === "B") {
                                            return <img key={index} style={{ width: '50px', height: '20px' }} src="/colores/negro.png" alt="Black Mana" class="mana-symbol" />;
                                            }

                                            if (symbol === "R") {
                                            return <img key={index} style={{ width: '50px', height: '20px' }} src="/colores/rojo.png" alt="Red Mana" class="mana-symbol" />;
                                            }

                                            if (symbol === "G") {
                                            return <img key={index} style={{ width: '50px', height: '20px' }} src="/colores/verde.png" alt="Green Mana" class="mana-symbol" />;
                                            }
                                            return <span key={index}>{symbol}</span>;
                                        })
    
                            }
                        </div>
                        

                        <h2>Type Line: {props.data.Carta_Recomendaciones.resultado.carta.type_line}</h2>
                        <h2>Oracle Text: {props.data.Carta_Recomendaciones.resultado.carta.oracle_text}</h2>
                        <div><a href={props.data.Carta_Recomendaciones.resultado.carta.purchase_uris.cardmarket} target="_blank" rel="noopener noreferrer">Comprar en Cardmarket</a></div>
                        <div><a href={props.data.Carta_Recomendaciones.resultado.carta.purchase_uris.tcgplayer} target="_blank" rel="noopener noreferrer">Comprar en TCGPlayer</a></div>
                        <div><p>Prices: {props.data.precios[5]} USD / {props.data.precios[6]} EUR</p></div>      
                        <div><p>Collection : {props.data.precios[2]}</p></div>          
                    </div>  
                </div>              
            }
        </div>
    );
}

export default Page;
