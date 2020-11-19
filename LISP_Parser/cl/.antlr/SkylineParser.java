// Generated from c:\Users\Edgar\Google Drive\Ingeniería informática\Q7\APA\APA-FIB\LISP_Parser\cl\Skyline.g by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class SkylineParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, NUM=12, WS=13, WORD=14;
	public static final int
		RULE_root = 0, RULE_assignment = 1, RULE_temp_skyline = 2, RULE_skyline = 3, 
		RULE_mirror = 4, RULE_intersection = 5, RULE_union = 6, RULE_translate_r = 7, 
		RULE_translate_l = 8, RULE_replicate = 9, RULE_existing_skyline = 10, 
		RULE_random_skyline = 11, RULE_building = 12, RULE_building_list = 13;
	private static String[] makeRuleNames() {
		return new String[] {
			"root", "assignment", "temp_skyline", "skyline", "mirror", "intersection", 
			"union", "translate_r", "translate_l", "replicate", "existing_skyline", 
			"random_skyline", "building", "building_list"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "':='", "'('", "')'", "'{'", "'}'", "'['", "']'", "'-'", "'*'", 
			"'+'", "','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			"NUM", "WS", "WORD"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Skyline.g"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public SkylineParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class RootContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(SkylineParser.EOF, 0); }
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public Temp_skylineContext temp_skyline() {
			return getRuleContext(Temp_skylineContext.class,0);
		}
		public RootContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_root; }
	}

	public final RootContext root() throws RecognitionException {
		RootContext _localctx = new RootContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_root);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(30);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				{
				setState(28);
				assignment();
				}
				break;
			case 2:
				{
				setState(29);
				temp_skyline();
				}
				break;
			}
			setState(32);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AssignmentContext extends ParserRuleContext {
		public TerminalNode WORD() { return getToken(SkylineParser.WORD, 0); }
		public SkylineContext skyline() {
			return getRuleContext(SkylineContext.class,0);
		}
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_assignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(34);
			match(WORD);
			setState(35);
			match(T__0);
			setState(36);
			skyline(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Temp_skylineContext extends ParserRuleContext {
		public SkylineContext skyline() {
			return getRuleContext(SkylineContext.class,0);
		}
		public Temp_skylineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_temp_skyline; }
	}

	public final Temp_skylineContext temp_skyline() throws RecognitionException {
		Temp_skylineContext _localctx = new Temp_skylineContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_temp_skyline);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(38);
			skyline(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SkylineContext extends ParserRuleContext {
		public List<SkylineContext> skyline() {
			return getRuleContexts(SkylineContext.class);
		}
		public SkylineContext skyline(int i) {
			return getRuleContext(SkylineContext.class,i);
		}
		public MirrorContext mirror() {
			return getRuleContext(MirrorContext.class,0);
		}
		public Existing_skylineContext existing_skyline() {
			return getRuleContext(Existing_skylineContext.class,0);
		}
		public Random_skylineContext random_skyline() {
			return getRuleContext(Random_skylineContext.class,0);
		}
		public Building_listContext building_list() {
			return getRuleContext(Building_listContext.class,0);
		}
		public BuildingContext building() {
			return getRuleContext(BuildingContext.class,0);
		}
		public UnionContext union() {
			return getRuleContext(UnionContext.class,0);
		}
		public IntersectionContext intersection() {
			return getRuleContext(IntersectionContext.class,0);
		}
		public TerminalNode NUM() { return getToken(SkylineParser.NUM, 0); }
		public Translate_rContext translate_r() {
			return getRuleContext(Translate_rContext.class,0);
		}
		public Translate_lContext translate_l() {
			return getRuleContext(Translate_lContext.class,0);
		}
		public ReplicateContext replicate() {
			return getRuleContext(ReplicateContext.class,0);
		}
		public SkylineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_skyline; }
	}

	public final SkylineContext skyline() throws RecognitionException {
		return skyline(0);
	}

	private SkylineContext skyline(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		SkylineContext _localctx = new SkylineContext(_ctx, _parentState);
		SkylineContext _prevctx = _localctx;
		int _startState = 6;
		enterRecursionRule(_localctx, 6, RULE_skyline, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(61);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				{
				setState(41);
				match(T__1);
				setState(42);
				skyline(0);
				setState(43);
				match(T__2);
				}
				break;
			case 2:
				{
				setState(45);
				mirror();
				setState(46);
				skyline(7);
				}
				break;
			case 3:
				{
				setState(48);
				existing_skyline();
				}
				break;
			case 4:
				{
				setState(49);
				match(T__3);
				setState(50);
				random_skyline();
				setState(51);
				match(T__4);
				}
				break;
			case 5:
				{
				setState(53);
				match(T__5);
				setState(54);
				building_list();
				setState(55);
				match(T__6);
				}
				break;
			case 6:
				{
				setState(57);
				match(T__1);
				setState(58);
				building();
				setState(59);
				match(T__2);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(80);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(78);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
					case 1:
						{
						_localctx = new SkylineContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_skyline);
						setState(63);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(66);
						_errHandler.sync(this);
						switch (_input.LA(1)) {
						case T__9:
							{
							setState(64);
							union();
							}
							break;
						case T__8:
							{
							setState(65);
							intersection();
							}
							break;
						default:
							throw new NoViableAltException(this);
						}
						setState(68);
						skyline(6);
						}
						break;
					case 2:
						{
						_localctx = new SkylineContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_skyline);
						setState(70);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(74);
						_errHandler.sync(this);
						switch (_input.LA(1)) {
						case T__9:
							{
							setState(71);
							translate_r();
							}
							break;
						case T__7:
							{
							setState(72);
							translate_l();
							}
							break;
						case T__8:
							{
							setState(73);
							replicate();
							}
							break;
						default:
							throw new NoViableAltException(this);
						}
						setState(76);
						match(NUM);
						}
						break;
					}
					} 
				}
				setState(82);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class MirrorContext extends ParserRuleContext {
		public MirrorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mirror; }
	}

	public final MirrorContext mirror() throws RecognitionException {
		MirrorContext _localctx = new MirrorContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_mirror);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(83);
			match(T__7);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IntersectionContext extends ParserRuleContext {
		public IntersectionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_intersection; }
	}

	public final IntersectionContext intersection() throws RecognitionException {
		IntersectionContext _localctx = new IntersectionContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_intersection);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(85);
			match(T__8);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class UnionContext extends ParserRuleContext {
		public UnionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_union; }
	}

	public final UnionContext union() throws RecognitionException {
		UnionContext _localctx = new UnionContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_union);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(87);
			match(T__9);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Translate_rContext extends ParserRuleContext {
		public Translate_rContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_translate_r; }
	}

	public final Translate_rContext translate_r() throws RecognitionException {
		Translate_rContext _localctx = new Translate_rContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_translate_r);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(89);
			match(T__9);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Translate_lContext extends ParserRuleContext {
		public Translate_lContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_translate_l; }
	}

	public final Translate_lContext translate_l() throws RecognitionException {
		Translate_lContext _localctx = new Translate_lContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_translate_l);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(91);
			match(T__7);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ReplicateContext extends ParserRuleContext {
		public ReplicateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_replicate; }
	}

	public final ReplicateContext replicate() throws RecognitionException {
		ReplicateContext _localctx = new ReplicateContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_replicate);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(93);
			match(T__8);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Existing_skylineContext extends ParserRuleContext {
		public TerminalNode WORD() { return getToken(SkylineParser.WORD, 0); }
		public Existing_skylineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_existing_skyline; }
	}

	public final Existing_skylineContext existing_skyline() throws RecognitionException {
		Existing_skylineContext _localctx = new Existing_skylineContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_existing_skyline);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(95);
			match(WORD);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Random_skylineContext extends ParserRuleContext {
		public List<TerminalNode> NUM() { return getTokens(SkylineParser.NUM); }
		public TerminalNode NUM(int i) {
			return getToken(SkylineParser.NUM, i);
		}
		public Random_skylineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_random_skyline; }
	}

	public final Random_skylineContext random_skyline() throws RecognitionException {
		Random_skylineContext _localctx = new Random_skylineContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_random_skyline);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(97);
			match(NUM);
			setState(98);
			match(T__10);
			setState(99);
			match(NUM);
			setState(100);
			match(T__10);
			setState(101);
			match(NUM);
			setState(102);
			match(T__10);
			setState(103);
			match(NUM);
			setState(104);
			match(T__10);
			setState(105);
			match(NUM);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BuildingContext extends ParserRuleContext {
		public List<TerminalNode> NUM() { return getTokens(SkylineParser.NUM); }
		public TerminalNode NUM(int i) {
			return getToken(SkylineParser.NUM, i);
		}
		public BuildingContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_building; }
	}

	public final BuildingContext building() throws RecognitionException {
		BuildingContext _localctx = new BuildingContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_building);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(107);
			match(NUM);
			setState(108);
			match(T__10);
			setState(109);
			match(NUM);
			setState(110);
			match(T__10);
			setState(111);
			match(NUM);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Building_listContext extends ParserRuleContext {
		public List<BuildingContext> building() {
			return getRuleContexts(BuildingContext.class);
		}
		public BuildingContext building(int i) {
			return getRuleContext(BuildingContext.class,i);
		}
		public Building_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_building_list; }
	}

	public final Building_listContext building_list() throws RecognitionException {
		Building_listContext _localctx = new Building_listContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_building_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(113);
			match(T__1);
			setState(114);
			building();
			setState(115);
			match(T__2);
			setState(123);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__10) {
				{
				{
				setState(116);
				match(T__10);
				setState(117);
				match(T__1);
				setState(118);
				building();
				setState(119);
				match(T__2);
				}
				}
				setState(125);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 3:
			return skyline_sempred((SkylineContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean skyline_sempred(SkylineContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 5);
		case 1:
			return precpred(_ctx, 6);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20\u0081\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\3\2\3\2\5\2!\n\2\3\2\3\2\3\3"+
		"\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3"+
		"\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5@\n\5\3\5\3\5\3\5\5\5E\n\5\3\5\3"+
		"\5\3\5\3\5\3\5\3\5\5\5M\n\5\3\5\3\5\7\5Q\n\5\f\5\16\5T\13\5\3\6\3\6\3"+
		"\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3"+
		"\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3"+
		"\17\3\17\3\17\3\17\7\17|\n\17\f\17\16\17\177\13\17\3\17\2\3\b\20\2\4\6"+
		"\b\n\f\16\20\22\24\26\30\32\34\2\2\2~\2 \3\2\2\2\4$\3\2\2\2\6(\3\2\2\2"+
		"\b?\3\2\2\2\nU\3\2\2\2\fW\3\2\2\2\16Y\3\2\2\2\20[\3\2\2\2\22]\3\2\2\2"+
		"\24_\3\2\2\2\26a\3\2\2\2\30c\3\2\2\2\32m\3\2\2\2\34s\3\2\2\2\36!\5\4\3"+
		"\2\37!\5\6\4\2 \36\3\2\2\2 \37\3\2\2\2!\"\3\2\2\2\"#\7\2\2\3#\3\3\2\2"+
		"\2$%\7\20\2\2%&\7\3\2\2&\'\5\b\5\2\'\5\3\2\2\2()\5\b\5\2)\7\3\2\2\2*+"+
		"\b\5\1\2+,\7\4\2\2,-\5\b\5\2-.\7\5\2\2.@\3\2\2\2/\60\5\n\6\2\60\61\5\b"+
		"\5\t\61@\3\2\2\2\62@\5\26\f\2\63\64\7\6\2\2\64\65\5\30\r\2\65\66\7\7\2"+
		"\2\66@\3\2\2\2\678\7\b\2\289\5\34\17\29:\7\t\2\2:@\3\2\2\2;<\7\4\2\2<"+
		"=\5\32\16\2=>\7\5\2\2>@\3\2\2\2?*\3\2\2\2?/\3\2\2\2?\62\3\2\2\2?\63\3"+
		"\2\2\2?\67\3\2\2\2?;\3\2\2\2@R\3\2\2\2AD\f\7\2\2BE\5\16\b\2CE\5\f\7\2"+
		"DB\3\2\2\2DC\3\2\2\2EF\3\2\2\2FG\5\b\5\bGQ\3\2\2\2HL\f\b\2\2IM\5\20\t"+
		"\2JM\5\22\n\2KM\5\24\13\2LI\3\2\2\2LJ\3\2\2\2LK\3\2\2\2MN\3\2\2\2NO\7"+
		"\16\2\2OQ\3\2\2\2PA\3\2\2\2PH\3\2\2\2QT\3\2\2\2RP\3\2\2\2RS\3\2\2\2S\t"+
		"\3\2\2\2TR\3\2\2\2UV\7\n\2\2V\13\3\2\2\2WX\7\13\2\2X\r\3\2\2\2YZ\7\f\2"+
		"\2Z\17\3\2\2\2[\\\7\f\2\2\\\21\3\2\2\2]^\7\n\2\2^\23\3\2\2\2_`\7\13\2"+
		"\2`\25\3\2\2\2ab\7\20\2\2b\27\3\2\2\2cd\7\16\2\2de\7\r\2\2ef\7\16\2\2"+
		"fg\7\r\2\2gh\7\16\2\2hi\7\r\2\2ij\7\16\2\2jk\7\r\2\2kl\7\16\2\2l\31\3"+
		"\2\2\2mn\7\16\2\2no\7\r\2\2op\7\16\2\2pq\7\r\2\2qr\7\16\2\2r\33\3\2\2"+
		"\2st\7\4\2\2tu\5\32\16\2u}\7\5\2\2vw\7\r\2\2wx\7\4\2\2xy\5\32\16\2yz\7"+
		"\5\2\2z|\3\2\2\2{v\3\2\2\2|\177\3\2\2\2}{\3\2\2\2}~\3\2\2\2~\35\3\2\2"+
		"\2\177}\3\2\2\2\t ?DLPR}";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}