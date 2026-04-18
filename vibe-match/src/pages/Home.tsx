import React, { useState, useEffect } from "react";
import { QUESTIONS, RESULTS } from "../constants/questions";

type Grade = keyof typeof RESULTS;

const Home: React.FC = () => {
  const [currentStep, setCurrentStep] = useState<"welcome" | "test" | "result">("welcome");
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [answers, setAnswers] = useState<number[]>([]);
  const [masterAnswers, setMasterAnswers] = useState<number[] | null>(null);
  const [shareLink, setShareLink] = useState("");

  const readDataParam = () => {
    const hash = window.location.hash;
    const hashQueryIndex = hash.indexOf("?");
    const hashQuery = hashQueryIndex >= 0 ? hash.slice(hashQueryIndex + 1) : "";
    const search = hashQuery || window.location.search.slice(1);
    const params = new URLSearchParams(search);
    return params.get("data");
  };

  useEffect(() => {
    const data = readDataParam();
    if (data) {
      try {
        const decoded = data.split("").map(Number);
        if (decoded.length === QUESTIONS.length) {
          setMasterAnswers(decoded);
        }
      } catch (e) {
        console.error("Failed to decode master answers", e);
      }
    }
  }, []);

  const handleStart = () => {
    setCurrentStep("test");
    setCurrentQuestionIndex(0);
    setAnswers([]);
  };

  const handleAnswer = (val: number) => {
    const newAnswers = [...answers];
    newAnswers[currentQuestionIndex] = val;
    setAnswers(newAnswers);

    if (currentQuestionIndex < QUESTIONS.length - 1) {
      setCurrentQuestionIndex(currentQuestionIndex + 1);
    } else {
      setCurrentStep("result");
      if (!masterAnswers) {
        // Master mode: generate link
        const dataStr = newAnswers.join("");
        const url = new URL(window.location.href);
        const baseUrl = `${url.origin}${url.pathname}`;
        setShareLink(`${baseUrl}#/?data=${dataStr}`);
      }
    }
  };

  const handleBack = () => {
    if (currentQuestionIndex > 0) {
      setCurrentQuestionIndex(currentQuestionIndex - 1);
    }
  };

  const calculateScore = () => {
    if (!masterAnswers) return 0;
    let score = 0;
    answers.forEach((ans, idx) => {
      const diff = Math.abs(ans - masterAnswers[idx]);
      if (diff === 0) score += 3;
      else if (diff === 1) score += 1;
      else if (diff === 2) score += 0;
      else if (diff === 3) score -= 1;
      else score -= 3;
    });
    return score;
  };

  const getGrade = (score: number): Grade => {
    if (score >= 50) return "卢俊舟爱你";
    if (score >= 20) return "是个人物";
    if (score >= -10) return "过门槛儿";
    if (score >= -40) return "路人";
    return "真不熟";
  };

  if (currentStep === "welcome") {
    return (
      <div className="min-h-screen bg-zinc-950 text-zinc-100 flex flex-col items-center justify-center p-6 text-center">
        <h1 className="text-3xl font-bold mb-4 text-purple-500">
          {masterAnswers ? "卢俊舟的灵魂匹配度考核" : "主人初始化：卢俊舟的灵魂档案"}
        </h1>
        <p className="text-zinc-400 mb-8 max-w-md">
          {masterAnswers 
            ? "你是否真的是卢俊舟的灵魂伴侣？通过 30 道天马行空的题目，测试你们的匹配度。" 
            : "Sam，请先完成这 30 道灵魂拷问，建立你的标准档案，随后即可生成分享链接。"}
        </p>
        <button
          onClick={handleStart}
          className="bg-purple-600 hover:bg-purple-700 text-white px-8 py-3 rounded-full font-bold transition-all transform hover:scale-105"
        >
          开始考核
        </button>
      </div>
    );
  }

  if (currentStep === "test") {
    const q = QUESTIONS[currentQuestionIndex];
    const progress = ((currentQuestionIndex + 1) / QUESTIONS.length) * 100;

    const dimensionColors: Record<string, string> = {
      "善恶观": "bg-purple-500",
      "价值观": "bg-blue-400",
      "金钱观": "bg-emerald-400",
      "消费观": "bg-orange-400",
      "人生观": "bg-white",
    };

    const dimensionTextColors: Record<string, string> = {
      "善恶观": "text-purple-400",
      "价值观": "text-blue-300",
      "金钱观": "text-emerald-300",
      "消费观": "text-orange-300",
      "人生观": "text-zinc-100",
    };

    const currentColor = dimensionColors[q.dimension] || "bg-purple-500";
    const currentTextColor = dimensionTextColors[q.dimension] || "text-purple-400";

    return (
      <div className="min-h-screen bg-zinc-950 text-zinc-100 flex flex-col items-center justify-center p-6">
        <div className="w-full max-w-xl">
          <div className="mb-8">
            <div className="flex justify-between items-center text-xs text-zinc-500 mb-2">
              <button 
                onClick={handleBack}
                className={`flex items-center hover:text-white transition-colors ${currentQuestionIndex === 0 ? 'invisible' : ''}`}
              >
                <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="15 19l-7-7 7-7" />
                </svg>
                上一题
              </button>
              <span className={`font-medium ${currentTextColor}`}>维度：{q.dimension}</span>
              <span>{currentQuestionIndex + 1} / {QUESTIONS.length}</span>
            </div>
            <div className="h-1 bg-zinc-800 rounded-full overflow-hidden">
              <div 
                className={`h-full transition-all duration-500 ease-out ${currentColor}`}
                style={{ width: `${progress}%` }}
              />
            </div>
          </div>

          <h2 className="text-xl md:text-2xl font-medium mb-12 text-center leading-relaxed">
            {q.text}
          </h2>

          <div className="space-y-4">
            { [
              { label: "非常赞同", val: 1 },
              { label: "赞同", val: 2 },
              { label: "不确定", val: 3 },
              { label: "不赞同", val: 4 },
              { label: "非常不赞同", val: 5 },
            ].map((opt) => {
              const isSelected = answers[currentQuestionIndex] === opt.val;
              return (
                <button
                  key={opt.val}
                  onClick={() => handleAnswer(opt.val)}
                  className={`w-full p-4 rounded-xl border transition-all text-left group ${
                    isSelected 
                      ? `border-current bg-current/20 text-white shadow-[0_0_15px_rgba(255,255,255,0.1)]` 
                      : "border-zinc-800 text-zinc-400 hover:border-zinc-500 hover:bg-zinc-500/10"
                  }`}
                  style={{ 
                    borderColor: isSelected ? currentColor.replace('bg-', '').replace('white', '#ffffff').replace('purple-500', '#a855f7').replace('blue-400', '#60a5fa').replace('emerald-400', '#34d399').replace('orange-400', '#fb923c') : undefined,
                    backgroundColor: isSelected ? `${currentColor.replace('bg-', '').replace('white', '#ffffff').replace('purple-500', '#a855f7').replace('blue-400', '#60a5fa').replace('emerald-400', '#34d399').replace('orange-400', '#fb923c')}20` : undefined
                  }}
                >
                  <div className="flex justify-between items-center">
                    <span>{opt.label}</span>
                    {isSelected && (
                      <div 
                        className="w-2 h-2 rounded-full shadow-[0_0_8px_rgba(255,255,255,0.5)]" 
                        style={{ backgroundColor: currentColor.replace('bg-', '').replace('white', '#ffffff').replace('purple-500', '#a855f7').replace('blue-400', '#60a5fa').replace('emerald-400', '#34d399').replace('orange-400', '#fb923c') }}
                      />
                    )}
                  </div>
                </button>
              );
            })}
          </div>
        </div>
      </div>
    );
  }

  const score = calculateScore();
  const grade = getGrade(score);

  return (
    <div className="min-h-screen bg-zinc-950 text-zinc-100 flex flex-col items-center justify-center p-6 text-center">
      <div className="max-w-xl">
        {masterAnswers ? (
          <>
            <div className="text-purple-500 text-sm font-bold mb-2 tracking-widest uppercase">匹配结果</div>
            <h1 className="text-4xl font-black mb-6">{grade}</h1>
            <div className="text-6xl font-black mb-8 text-zinc-800">{score}</div>
            <p className="text-zinc-400 text-lg leading-relaxed mb-12">
              {RESULTS[grade]}
            </p>
            <button
              onClick={() => window.location.reload()}
              className="text-zinc-500 hover:text-white transition-colors"
            >
              重新测试
            </button>
          </>
        ) : (
          <>
            <h1 className="text-3xl font-bold mb-6 text-green-500">✅ 档案建立成功</h1>
            <p className="text-zinc-400 mb-8">
              Sam，你的灵魂数据已加密到链接中。复制下方链接发给朋友，看看谁才是你的真命天子。
            </p>
            <div className="bg-zinc-900 p-4 rounded-xl border border-zinc-800 break-all text-sm text-zinc-300 mb-8">
              {shareLink}
            </div>
            <button
              onClick={() => {
                navigator.clipboard.writeText(shareLink);
                alert("链接已复制到剪贴板！");
              }}
              className="bg-purple-600 hover:bg-purple-700 text-white px-8 py-3 rounded-full font-bold transition-all"
            >
              复制分享链接
            </button>
          </>
        )}
      </div>
    </div>
  );
};

export default Home;
