import { FreshContext, Handlers,PageProps } from "$fresh/server.ts";
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
            image_uris: {
                normal: string;
            }
            purchase_uris: {
                cardmarket: string;
                tcgplayer: string;
            }
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

export const handler:Handlers = {
    GET:async (req:Request,ctx:FreshContext<unknown,Carta_Recomendaciones>) => {
        const response = await fetch("http://localhost:8001/escanear_carta", {
            method: "GET",
        });
        if (!response.ok) {
            console.log("Error al escanear la carta", "error");
            console.error("Error al escanear la carta:", response.statusText);
            return ctx.render("");
        }

        const data:Carta_Recomendaciones = await response.json();
        console.log(data);

              
        if (!data.resultado) {
            console.log("Error al escanear la carta", "error");
            console.error("Error al escanear la carta 2 :", response.statusText);
            return ctx.render(""); 
        }
        return ctx.render(data);
        // console.log(data.resultado);
       
       
        
      
        
    }
}

const Page = (props:PageProps<Carta_Recomendaciones>) => {
    
    return (
        <div>
            <form method="GET" action="/escanear">
                <button type="submit">Escanear carta</button>
            </form>  
                      
            {props.data === "" ? <p>No se ha podido escanear la carta</p> :
            <div>
                <img src={props.data.resultado.carta.image_uris.normal} alt="Carta escaneada" />
                <div>
                    <h2>Nanme: {props.data.resultado.carta.name}</h2>
                    <h2>Mana Cost: {props.data.resultado.carta.mana_cost}</h2>
                    <div><a href={props.data.resultado.carta.purchase_uris.cardmarket} target="_blank" rel="noopener noreferrer">Comprar en Cardmarket</a></div>
                    <div><a href={props.data.resultado.carta.purchase_uris.tcgplayer} target="_blank" rel="noopener noreferrer">Comprar en TCGPlayer</a></div>
                    
                    
                </div>
            </div>    
            }
        </div>
    );
}

export default Page;
