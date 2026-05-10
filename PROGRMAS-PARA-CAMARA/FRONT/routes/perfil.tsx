import { FreshContext, Handlers,PageProps } from "$fresh/server.ts";
import { get_all_cards, get_collection_cards, get_unique_collections } from "../bbdd/conexion.tsx";
import Zona_usuario from "../islands/Perfil.tsx";
export type card ={
    img: string;
    coleccion: string;
}
export type collection_card = {
    card : card[];
    collections: string [];
}
export const handler: Handlers = {
    GET: async (req: Request, ctx: FreshContext<unknown, collection_card>) => {
        const cards: card[] = await get_all_cards()
        const colecctions :string[] = await get_unique_collections()
        console.log(cards)
        console.log("----------------")
        console.log(colecctions)
        return ctx.render ({card: cards , collections: colecctions})
    }
}

const Page = (props: PageProps<collection_card>) => {
    return (
        <Zona_usuario card ={props.data.card} collections = {props.data.collections}/>
    )
}

export default Page