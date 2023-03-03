// Generated from main/mp/parser/MP.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link MPParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface MPVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link MPParser#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgram(MPParser.ProgramContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#vardecls}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVardecls(MPParser.VardeclsContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#vardecltail}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVardecltail(MPParser.VardecltailContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#vardecl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVardecl(MPParser.VardeclContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#mptype}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMptype(MPParser.MptypeContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#ids}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIds(MPParser.IdsContext ctx);
}